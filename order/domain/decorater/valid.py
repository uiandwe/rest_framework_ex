# -*- coding: utf-8 -*-
import inspect
import typing


class Valid:
    def validtion(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        class_field = dict()
        for attr in attributes:
            if attr[0] == '__annotations__':
                class_field = attr[1]
                break

        for key in class_field.keys():

            if isinstance(class_field[key], typing.GenericMeta):
                continue
            # print(key, class_field[key], self.__getattribute__(key), type(class_field[key]))

            if not isinstance(self.__getattribute__(key), class_field[key]):
                raise TypeError(
                    'Unexpected type for {} (expected {} but found {})'.format(key, class_field[key], type(self.__getattribute__(key))))

