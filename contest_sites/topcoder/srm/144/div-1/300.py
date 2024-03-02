#!/usr/bin/env python3

class BinaryCode:
    def decode(self, message):
        if len(message) == 1:
            if message == '0':
                return ('0', 'NONE')
            elif message == '1':
                return ('NONE', '1')
            else:
                return ('NONE', 'NONE')
        else:
            a = self.decode_with_setting_first_value(message, 0)
            b = self.decode_with_setting_first_value(message, 1)
            return (a, b)

    def is_value_0_or_1(self, x):
        if x == 0 or x == 1:
            return True
        else:
            return False

    def decode_with_setting_first_value(self, message, first_value):
        q = list(map(int, list(message)))
        p = [0] * len(q)
        p[0] = first_value

        p[1] = q[0] - p[0]
        if not self.is_value_0_or_1(p[1]):
            return 'NONE'

        for i in range(2, len(q)):
            p[i] = q[i-1] - p[i-1] - p[i-2]
            if not self.is_value_0_or_1(p[i]):
                return 'NONE'

        if q[-1] != p[-2] + p[-1]:
            return 'NONE'

        decoded_message = ''.join(map(str, p))
        return decoded_message



if __name__ == '__main__':
    b = BinaryCode()
    # print(b.decode('0'))
    # print(b.decode('1'))
    # print(b.decode('2'))
    print(b.decode('00'))
    print(b.decode('11'))
    print(b.decode('22'))
    print(b.decode('33'))
    print(b.decode('0000'))
    print(b.decode('111'))
    print(b.decode('121'))
    print(b.decode('122'))
    print(b.decode('221'))
