STRING = "Makes text look like this."


def spongebobify( string ):

    character_index = 0
    actual_index = 0
    while( actual_index < len( string ) ):
        if( not string[actual_index].isalpha() ):
            pass
        else:
            string = change_character( string, character_index, actual_index )
            character_index += 1
        actual_index += 1

    return string


def change_character( string, character_index, actual_index ):
    if( character_index % 2 ):
        return lower_character( string, actual_index )
    else:
        return upper_character( string, actual_index )


def lower_character( string, index ):
    if( index == len( string ) - 1 ):
        return string[0:index] + string[index].lower()
    else:
        return string[0:index] + string[index].lower() + string[index + 1::]


def upper_character( string, index ):
    if( index == len( string ) - 1 ):
        return string[0:index] + string[index].upper()
    else:
        return string[0:index] + string[index].upper() + string[index + 1::]


if( __name__ == "__main__" ):
    print( spongebobify( STRING ) )
