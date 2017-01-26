#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random


def getRandomFortune():
    # list of possible fortunes
    fortunes = [
        "Think before you do and all will win.",
        "Everything has its beauty, but not everyone sees it.",
        "It does not matter how slowly you go so long as you do not stop.",
        "Our greatest glory is not in never falling, but in rising every time we fall.",
    ]

    # randomly select one of the fortunes
    index = random.randint(0, 3)


    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: <br>Confucius says: "+ fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        number_sentence = 'Your Lucky number: ' + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"

        new_cookie_button = "<a href='.'><button>Another Cookie Please!</button></a>"

        content = header + fortune_paragraph + number_paragraph + new_cookie_button
        self.response.write(content)


routes = [
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
