# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from platformio.managers.platform import PlatformBase
from platformio.util import get_systype

class Espressif8266idfPlatform(PlatformBase):

    def configure_default_packages(self, variables, targets):
        if not variables.get("pioframework"):
            self.packages['sdk-esp8266']['optional'] = False
        if "buildfs" in targets:
            self.packages['tool-mkspiffs']['optional'] = False
        if "esp8266-rtos-sdk-idf" in variables.get("pioframework", []):
            for p in self.packages:
                if p in ("tool-cmake", "tool-ninja"):
                    self.packages[p]["optional"] = False
                elif p in ("tool-mconf") and "windows" in get_systype():
                    self.packages[p]['optional'] = False
        return PlatformBase.configure_default_packages(
            self, variables, targets)
