#-----------------------------------------------------------------------------
# Make Anything Makefile
#-----------------------------------------------------------------------------
# For use with GNU Make
#
# The only prerequisite to using this Makefile is that the program source
# files all reside in their own directory, with only ONE of these source
# files declaring main(). For example,
#
#   my_last_nameHW3/
#     Makefile                 <-- "make anything" makefile
#     linked_list.h
#     linked_list.cxx          <-- the file the student modifies
#     node.h
#     test_linked_list.cxx     <-- the file containing the main() function.
#
# This makefile will correctly identify the files and produce:
#
#   linked_list.o
#   test_linked_list.o
#
# and then the executable
#
#   test_linked_list*
#
# The orphan "node.h" is included in every source module's prerequisites,
# regardless of whether it is actually used by that module.
#
#-----------------------------------------------------------------------------
# When MIXING C and C++ modules, this makefile will compile the C modules
# with the C compiler, and the C++ modules with the C++ compiler. Keep that
# in mind! (Also, the linking stage will be done with the C++ compiler.)
#
#-----------------------------------------------------------------------------
# "make clean" works as usual.
# "make cleaner" works better than usual.
#
# --Michael
#
#-----------------------------------------------------------------------------
# general options
#-----------------------------------------------------------------------------
# These are the names of the C and C++ compilers to use, and options common
# to both compilers.
#
# If you want to specify an option specific to only one of the compilers,
# just place it after the compiler name. For example:
#   CPP = g++ -fno-elide-constructors
#
CCC     = gcc
CPP     = g++
CFLAGS  = -Wall -g -std=c++11 -O2
LDFLAGS =
#-----------------------------------------------------------------------------
# valid C++ file extensions
#-----------------------------------------------------------------------------
# These are the list of acceptable C++ extensions. If you want to support
# some non-standard C++ extension not listed here, just add it to this list.
#
CPP_EXTS = cpp cxx cc C c++
#-----------------------------------------------------------------------------
# don't mess with these definitions
#-----------------------------------------------------------------------------
CCC_SOURCE_FILES = $(wildcard *.c)
CPP_SOURCE_FILES = $(wildcard $(foreach ext, $(CPP_EXTS), *.$(ext)))
SOURCE_FILES     = $(CCC_SOURCE_FILES) $(CPP_SOURCE_FILES)
ifeq ($(CPP_SOURCE_FILES),)
CC = $(CCC)
else
CC = $(CPP)
endif
#-----------------------------------------------------------------------------
# orphan header files
#-----------------------------------------------------------------------------
# Any header files with no corresponding code file.
#
ORPHAN_H = $(filter-out $(addsuffix .h, $(basename $(SOURCE_FILES))), $(wildcard *.h))
#-----------------------------------------------------------------------------
# object files
#-----------------------------------------------------------------------------
# These lists are generated from the source code files, meaning that if
# "foo.cxx" (or whatever the specified extention is) exists then "foo.o"
# is included in this list.
#
CCC_OBJS = $(addsuffix .o, $(basename $(CCC_SOURCE_FILES)))
CPP_OBJS = $(addsuffix .o, $(basename $(CPP_SOURCE_FILES)))
ALL_OBJS = $(CCC_OBJS) $(CPP_OBJS)
#-----------------------------------------------------------------------------
# exe name
#-----------------------------------------------------------------------------
# This is the name of the executable we are creating. It is generated
# using the grep utility to find the file containing the main function.
#
# The regular expression is this:
#   beginning of line may contain whitespace
#   first non-whitespace character in line may not be /
#   any other non-whitespace characters OK
#   next word must be 'main'
#   followed by optional whitespace
#   followed by '('
#
# Limitations
#   This cannot account for multi-line comments where the word 'main' followed
#   by '(' appears and does not have a '/*' or '//' at the beginning of the
#   line.
#
grep_cmd = grep -l '^[ \t\v]*[^/]*.*\<main[ \t\v]*(' $(SOURCE_FILES)
BIN_NAME = $(basename $(shell $(grep_cmd)))
ifneq ($(words $(BIN_NAME)),1)
$(error Only one file may use the word 'main(' ))
endif
#-----------------------------------------------------------------------------
# function to convert foo.o to foo.cpp
#-----------------------------------------------------------------------------
# arguments
#   $(1)  the name of the object file, e.g. "foo.o"
#
obj_to_src = $(foreach name, $(foreach ext, $(CPP_EXTS), $(addsuffix .$(ext), $(basename $(1)))), $(filter $(name), $(CPP_SOURCE_FILES)))
#-----------------------------------------------------------------------------
# MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
#-----------------------------------------------------------------------------
# This rule is for the default target, which is to compile the program
# (whatever it may be). If the program itself has a header file it is
# listed as a prerequisite.
#
$(BIN_NAME): $(ALL_OBJS) $(filter $(BIN_NAME).h, $(wildcard *.h))
	$(CC) $(CFLAGS) $(ALL_OBJS) $(LDFLAGS) -o $(BIN_NAME)
#-----------------------------------------------------------------------------
# individual source modules
#-----------------------------------------------------------------------------
# This rule compiles each source file into an object file. If a header file
# corresponding to the source file exists (i.e. "code.cxx" and "code.h") it
# is included in the prerequisites. (That way the source file is properly
# recompiled if the header file is changed.)
#
ifneq ($(CCC_OBJS),)
$(CCC_OBJS): $(addsuffix .c, $(*F)) $(filter $(addsuffix .h, $(basename $@)), $(wildcard *.h)) $(ORPHAN_H)
	$(CCC) $(CFLAGS) -c $(addsuffix .c, $(*F)) -o $@
endif
ifneq ($(CPP_OBJS),)
$(CPP_OBJS): $(call obj_to_src, $@) $(filter $(addsuffix .h, $(basename $@)), $(wildcard *.h)) $(ORPHAN_H)
	$(CPP) $(CFLAGS) -c $(call obj_to_src, $@) -o $@
endif
#-----------------------------------------------------------------------------
# cleanup
#-----------------------------------------------------------------------------
.PHONY: clean
clean: FORCE
	rm -f *.o
.PHONY: cleaner
cleaner: FORCE
	rm -f *.o $(BIN_NAME)
FORCE:
#end Makefile