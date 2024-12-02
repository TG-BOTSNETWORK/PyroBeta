#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import base64
import struct
from typing import List, Tuple


class Storage:
    OLD_SESSION_STRING_FORMAT = ">B?256sI?"
    NEW_SESSION_STRING_FORMAT = ">BCT?7Si"
    SESSION_STRING_SIZE = 351
    SESSION_STRING_SIZE_64 = 356

    SESSION_STRING_FORMAT = ">BCT?7Si"

    def __init__(self, name: str):
        self.name = name

    async def open(self):
        raise NotImplementedError("The `open` method is not implemented")

    async def save(self):
        raise NotImplementedError("The `save` method is not implemented")

    async def close(self):
        raise NotImplementedError("The `close` method is not implemented")

    async def delete(self):
        raise NotImplementedError("The `delete` method is not implemented")

    async def update_peers(self, peers: List[Tuple[int, int, str, str, str]]):
        raise NotImplementedError("The `update_peers` method is not implemented")

    async def get_peer_by_id(self, peer_id: int):
        raise NotImplementedError("The `get_peer_by_id` method is not implemented")

    async def get_peer_by_username(self, username: str):
        raise NotImplementedError("The `get_peer_by_username` method is not implemented")

    async def get_peer_by_phone_number(self, phone_number: str):
        raise NotImplementedError("The `get_peer_by_phone_number` method is not implemented")

    async def dc_id(self, value: int = object):
        raise NotImplementedError("The `dc_id` method is not implemented")

    async def api_id(self, value: int = object):
        raise NotImplementedError("The `api_id` method is not implemented")

    async def test_mode(self, value: bool = object):
        raise NotImplementedError("The `test_mode` method is not implemented")

    async def auth_key(self, value: bytes = object):
        raise NotImplementedError("The `auth_key` method is not implemented")

    async def date(self, value: int = object):
        raise NotImplementedError("The `date` method is not implemented")

    async def user_id(self, value: int = object):
        raise NotImplementedError("The `user_id` method is not implemented")

    async def is_bot(self, value: bool = object):
        raise NotImplementedError("The `is_bot` method is not implemented")

    async def export_session_string(self):
        try:
            packed = struct.pack(
                self.SESSION_STRING_FORMAT,
                await self.dc_id(),
                await self.api_id(),
                await self.test_mode(),
                await self.auth_key(),
                await self.user_id(),
                await self.is_bot()
            )
            return base64.urlsafe_b64encode(packed).decode().rstrip("=")
        except Exception as e:
            raise RuntimeError(f"Failed to export session string: {e}")
