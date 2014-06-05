#!/bin/bash
# set the IDL directories.
IDL_DIR=/Applications/rsi/idl; export IDL_DIR
ASTIDLUTIL=/Users/holden; export ASTIDLUTIL
# These IDL directories will likely differ for you...check with your system administrator.

# clear the path.
IDL_PATH=''
# add the base IDL library and examples to path.
# this is needed for some basic utilities
IDL_PATH=$IDL_DIR/lib

# essential directories for XIDL and GODDARD stuff
IDLUTILS_DIR=$ASTIDLUTIL/idl/idlutils; export IDLUTILS_DIR
XIDL_DIR=$ASTIDLUTIL/idl/xidl/; export XIDL_DIR

IDL_PATH=$IDL_PATH:$XIDL_DIR/Obs/Sky/
IDL_PATH=$IDL_PATH:$XIDL_DIR/Obs/S2N/
IDL_PATH=$IDL_PATH:$XIDL_DIR/Obs/
IDL_PATH=$IDL_PATH:$XIDL_DIR/General/
IDL_PATH=$IDL_PATH:$IDLUTILS_DIR/goddard/pro/fits/
IDL_PATH=$IDL_PATH:$IDLUTILS_DIR/goddard/pro/fits_bintable/
IDL_PATH=$IDL_PATH:$IDLUTILS_DIR/goddard/pro/misc/
IDL_PATH=$IDL_PATH:$IDLUTILS_DIR/goddard/pro/structure/
export IDL_PATH

TEMPLATE_DIR=$ASTIDLUTIL/templates/; export TEMPLATE_DIR
FILTER_DIR=$ASTIDLUTIL/filters/; export FILTER_DIR


