import shutil
import subprocess

from django.test import TestCase
from django.conf import settings

from .models import Video


class VideoTestCase(TestCase):
    def test_ffmpeg_command_exists(self):
        self.assertTrue(shutil.which('ffmpeg'), 'ffmpeg does not exist')

        command_list = [
            'ffmpeg',
            '-i',
            'media/test.mp4',
            '-vf',
            'scale=-1:240',
            '-c:v',
            'libx264',
            '-c:a',
            'copy',
            'media/test_240.mp4',
        ]

        # run for scale 240
        self.assertEqual(subprocess.call(command_list), 0)
        
        # run for scale 360
        command_list[4] = 'scale=-1:360'
        command_list[-1] = 'media/test_360.mp4'
        self.assertEqual(subprocess.call(command_list), 0)

    def test_redis_connection(self):
        command_list = [
            'redis-cli',
            'ping',
        ]

        print(subprocess.call(command_list))
