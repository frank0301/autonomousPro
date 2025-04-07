# generated from rosidl_generator_py/resource/_idl.py.em
# with input from common_interface:msg/KeyCtrl.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_KeyCtrl(type):
    """Metaclass of message 'KeyCtrl'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('common_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'common_interface.msg.KeyCtrl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__key_ctrl
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__key_ctrl
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__key_ctrl
            cls._TYPE_SUPPORT = module.type_support_msg__msg__key_ctrl
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__key_ctrl

            from geometry_msgs.msg import Twist
            if Twist.__class__._TYPE_SUPPORT is None:
                Twist.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class KeyCtrl(metaclass=Metaclass_KeyCtrl):
    """Message class 'KeyCtrl'."""

    __slots__ = [
        '_allow_nav',
        '_manual_spd',
    ]

    _fields_and_field_types = {
        'allow_nav': 'boolean',
        'manual_spd': 'geometry_msgs/Twist',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Twist'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.allow_nav = kwargs.get('allow_nav', bool())
        from geometry_msgs.msg import Twist
        self.manual_spd = kwargs.get('manual_spd', Twist())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.allow_nav != other.allow_nav:
            return False
        if self.manual_spd != other.manual_spd:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def allow_nav(self):
        """Message field 'allow_nav'."""
        return self._allow_nav

    @allow_nav.setter
    def allow_nav(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'allow_nav' field must be of type 'bool'"
        self._allow_nav = value

    @builtins.property
    def manual_spd(self):
        """Message field 'manual_spd'."""
        return self._manual_spd

    @manual_spd.setter
    def manual_spd(self, value):
        if __debug__:
            from geometry_msgs.msg import Twist
            assert \
                isinstance(value, Twist), \
                "The 'manual_spd' field must be a sub message of type 'Twist'"
        self._manual_spd = value
