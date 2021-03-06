#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
# pylint: disable=no-self-use
"""This module contains the auxiliary class ContextTypes."""
from typing import Type, Generic, overload, Dict, TYPE_CHECKING  # pylint: disable=unused-import

from telegram.ext._callbackcontext import CallbackContext
from telegram.ext._utils.types import CCT, UD, CD, BD

if TYPE_CHECKING:
    from telegram.ext._extbot import ExtBot  # pylint: disable=unused-import


class ContextTypes(Generic[CCT, UD, CD, BD]):
    """
    Convenience class to gather customizable types of the :class:`telegram.ext.CallbackContext`
    interface.

    .. versionadded:: 13.6

    Args:
        context (:obj:`type`, optional): Determines the type of the ``context`` argument of all
            (error-)handler callbacks and job callbacks. Must be a subclass of
            :class:`telegram.ext.CallbackContext`. Defaults to
            :class:`telegram.ext.CallbackContext`.
        bot_data (:obj:`type`, optional): Determines the type of
            :attr:`context.bot_data <CallbackContext.bot_data>` of all (error-)handler callbacks
            and job callbacks. Defaults to :obj:`dict`. Must support instantiating without
            arguments.
        chat_data (:obj:`type`, optional): Determines the type of
            :attr:`context.chat_data <CallbackContext.chat_data>` of all (error-)handler callbacks
            and job callbacks. Defaults to :obj:`dict`. Must support instantiating without
            arguments.
        user_data (:obj:`type`, optional): Determines the type of
            :attr:`context.user_data <CallbackContext.user_data>` of all (error-)handler callbacks
            and job callbacks. Defaults to :obj:`dict`. Must support instantiating without
            arguments.

    """

    __slots__ = ('_context', '_bot_data', '_chat_data', '_user_data')

    # overload signatures generated with
    # https://gist.github.com/Bibo-Joshi/399382cda537fb01bd86b13c3d03a956

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, Dict, Dict, Dict], Dict, Dict, Dict]',
    ):
        ...

    @overload
    def __init__(self: 'ContextTypes[CCT, Dict, Dict, Dict]', context: Type[CCT]):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, UD, Dict, Dict], UD, Dict, Dict]',
        user_data: Type[UD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, Dict, CD, Dict], Dict, CD, Dict]',
        chat_data: Type[CD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, Dict, Dict, BD], Dict, Dict, BD]',
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, UD, Dict, Dict]', context: Type[CCT], user_data: Type[UD]
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, Dict, CD, Dict]', context: Type[CCT], chat_data: Type[CD]
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, Dict, Dict, BD]', context: Type[CCT], bot_data: Type[BD]
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, UD, CD, Dict], UD, CD, Dict]',
        user_data: Type[UD],
        chat_data: Type[CD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, UD, Dict, BD], UD, Dict, BD]',
        user_data: Type[UD],
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, Dict, CD, BD], Dict, CD, BD]',
        chat_data: Type[CD],
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, UD, CD, Dict]',
        context: Type[CCT],
        user_data: Type[UD],
        chat_data: Type[CD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, UD, Dict, BD]',
        context: Type[CCT],
        user_data: Type[UD],
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, Dict, CD, BD]',
        context: Type[CCT],
        chat_data: Type[CD],
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CallbackContext[ExtBot, UD, CD, BD], UD, CD, BD]',
        user_data: Type[UD],
        chat_data: Type[CD],
        bot_data: Type[BD],
    ):
        ...

    @overload
    def __init__(
        self: 'ContextTypes[CCT, UD, CD, BD]',
        context: Type[CCT],
        user_data: Type[UD],
        chat_data: Type[CD],
        bot_data: Type[BD],
    ):
        ...

    def __init__(  # type: ignore[no-untyped-def]
        self,
        context=CallbackContext,
        bot_data=dict,
        chat_data=dict,
        user_data=dict,
    ):
        if not issubclass(context, CallbackContext):
            raise ValueError('context must be a subclass of CallbackContext.')

        # We make all those only accessible via properties because we don't currently support
        # changing this at runtime, so overriding the attributes doesn't make sense
        self._context = context
        self._bot_data = bot_data
        self._chat_data = chat_data
        self._user_data = user_data

    @property
    def context(self) -> Type[CCT]:
        """The type of the ``context`` argument of all (error-)handler callbacks and job
        callbacks.
        """
        return self._context

    @property
    def bot_data(self) -> Type[BD]:
        """The type of :attr:`context.bot_data <CallbackContext.bot_data>` of all (error-)handler
        callbacks and job callbacks.
        """
        return self._bot_data

    @property
    def chat_data(self) -> Type[CD]:
        """The type of :attr:`context.chat_data <CallbackContext.chat_data>` of all (error-)handler
        callbacks and job callbacks.
        """
        return self._chat_data

    @property
    def user_data(self) -> Type[UD]:
        """The type of :attr:`context.user_data <CallbackContext.user_data>` of all (error-)handler
        callbacks and job callbacks.
        """
        return self._user_data
