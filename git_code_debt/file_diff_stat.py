    BINARY = object()
        'FileDiffStat',
        ['path', 'lines_added', 'lines_removed', 'status', 'special_file'],
    is_binary = False
        elif line.startswith('Binary files'):
            is_binary = True
        elif line.startswith('--- ') and not in_diff:
            pass
    elif is_binary:
        special_file = SpecialFile(
            file_type=SpecialFileType.BINARY,
            added=diff_line_filename if status is not Status.DELETED else None,
            removed=diff_line_filename if status is not Status.ADDED else None,
        )
    return [_to_file_diff_stat(file_diff) for file_diff in files[1:]]