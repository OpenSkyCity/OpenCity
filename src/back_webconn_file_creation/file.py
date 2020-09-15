def file_read(input_file, **kwargs):
    as_list = kwargs.pop('as_list', False)
    with open(input_file, "r", **kwargs) as __in__:
        # print([data.replace('\n', '') for data in __in__.readlines()])
        return [data.replace('\n', '') for data in __in__.readlines()] if as_list else __in__.read()


def file_write(output_file, content, **kwargs):
    with open(output_file, "w", **kwargs) as __in__:
        __in__.write(content)


def file_append(output_file, content, **kwargs):
    with open(output_file, "a", **kwargs) as __in__:
        __in__.write(content)


def binary_file_read(input_file, **kwargs):
    as_list = kwargs.pop('as_list')
    with open(input_file, "rb", **kwargs) as __in__:
        return [data.replace(b'\n', b'') for data in __in__.readlines()] if as_list else __in__.read()


def binary_file_write(output_file, bytes_1, **kwargs):
    with open(output_file, "wb", **kwargs) as __in__:
        __in__.write(bytes_1)


def binary_file_append(output_file, bytes_1, **kwargs):
    with open(output_file, "ab", **kwargs) as __in__:
        __in__.write(bytes_1)


def file_copy(input_file, output_file, **kwargs):
    with open(input_file, "r", **kwargs) as input_:
        with open(output_file, 'w', **kwargs) as output:
            for i in input_:
                output.write(i)


def binary_file_copy(input_file, output_file, **kwargs):
    with open(input_file, "rb", **kwargs) as input_:
        with open(output_file, 'wb', **kwargs) as output:
            for i in input_:
                output.write(i)
