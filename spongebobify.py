# ------------------------------------------------------------------------------
# Imports ----------------------------------------------------------------------
# ------------------------------------------------------------------------------

import sys


# ------------------------------------------------------------------------------
# Functions --------------------------------------------------------------------
# ------------------------------------------------------------------------------

def spongebobify( string ):
    # Keeps track of how many characters have been changed.
    character_index = 0
    # Keeps track of the current place in the string.
    actual_index = 0

    while( actual_index < len( string ) ):
        if( string[actual_index].isalpha() ):
            string = change_character( string, character_index, actual_index )
            character_index += 1

        actual_index += 1

    return string


# ------------------------------------------------------------------------------
# Helper Functions -------------------------------------------------------------
# ------------------------------------------------------------------------------

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


# ------------------------------------------------------------------------------
# Main -------------------------------------------------------------------------
# ------------------------------------------------------------------------------

if( __name__ == "__main__" ):
    arguments = sys.argv

    if( len( arguments ) > 2 ):
        print( "This function only takes 1 argument.")
    elif( len( arguments ) == 1 ):
        print( "Must pass in a string." )
    elif( type( arguments[1] ) != type( "" ) ):
        print( "Must enter a string." )
    else:
        print( spongebobify( arguments[1] ) )
