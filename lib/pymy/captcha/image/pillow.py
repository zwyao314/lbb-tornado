import hashlib
import math
import random
from constant import ROOT_PATH
from lib.pymy.captcha.concern.abstract_image_captcha import AbstractImageCaptcha
from lib.pymy.session.session import Session
from lib.pymy.stdlib.date_time import DateTime
from os import makedirs
from os.path import isdir, join as path_join, realpath
from PIL import Image, ImageDraw, ImageFont


class Pillow(AbstractImageCaptcha):

    @classmethod
    def new(cls, options: dict = {}):
        me = cls()
        me.id = options['id'] if 'id' in options else None
        me.char_list = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        me.phrase_length = 6
        me.web_path = "."
        me.image_folder = "media/captcha"
        me.width = 220
        me.height = 40

        return me

    def generate(self) -> str:
        code = random.sample(self.char_list, self.phrase_length)
        code = ''.join(code)
        self._session(self.get_id(), code)

        background_color = (
            random.randint(0, 150),
            random.randint(0, 150),
            random.randint(0, 150)
        )
        im = Image.new(
            mode="RGB",
            size=(self.get_width(),
                  self.get_height()),
            color=background_color
        )
        font_size = random.randint(24, 40)
        im_font = ImageFont.truetype(
            font=path_join(ROOT_PATH, 'resources', 'font', 'AlibabaSans-Light.otf'),
            size=font_size
        )
        text_xy = (
            random.randint(0, math.floor(self.get_width() * 0.3)),
            0
        )
        im_draw = ImageDraw.Draw(im)
        im_draw.text(
            xy=text_xy,
            text=code,
            font=im_font,
            align="center"
        )
        # line_begin = (
        #     random.randint(0, self.get_width() * 0.5),
        #     random.randint(0, self.get_height())
        # )
        # line_end = (
        #     random.randint(self.get_width() * 0.5, self.get_width()),
        #     random.randint(0, self.get_height())
        # )
        line_color = (
            random.randint(0, 250),
            random.randint(0, 250),
            random.randint(0, 250)
        )
        # im_draw.line(
        #     xy=[line_begin, line_end],
        #     fill=line_color,
        #     width=self.get_width()
        # )
        for w in range(self.get_width()):
            for h in range(self.get_height()):
                temp_chance = random.randint(0, 100)
                if temp_chance < 20:
                    im_draw.point(xy=(w, h), fill=line_color)
        # im.show()
        file_name = self._unique_hash_id() + ".png"
        file_path = self.web_path + '/' + self.image_folder
        file_path = realpath(file_path)
        file = file_path + '/' + file_name
        if not isdir(file_path):
            makedirs(file_path, mode=0o777)
        im.save(file, format="png")
        del im, im_font, im_draw

        return '/' + self.image_folder + '/' + file_name

    def validate_phrase(self, user_phrase: str) -> bool:
        code = self._session(self.get_id())
        code = code.lower()
        user_phrase = user_phrase.lower()

        return user_phrase == code

    def get_id(self) -> str:
        id = self.id
        if id is None:
            id = self.generate_id()
            self.id = id

        return id

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def _session(self, key=None, value=None):
        session = Session.session()
        if key is None:
            return session
        elif value is None:
            return session.get(key)
        elif value is not None:
            session.set(key, value)

    def generate_id(self) -> str:
        return self._unique_hash_id()

    def _unique_hash_id(self) -> str:
        b_hash_text = str(DateTime.now()).encode() + '|'.encode() + random.randbytes(40)
        id = hashlib.md5(b_hash_text).hexdigest()

        return id

    def set_web_path(self, path: str):
        self.web_path = path

        return self
