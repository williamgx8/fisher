#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def set_key(q: str) -> str:
    if q.isdigit() and len(q) == 13:
        return 'isbn'
    short_q = q.replace('-', '')
    if short_q.isdigit() and len(short_q) == 10:
        return 'isbn'
    return 'key'
