CC=gcc
CXX=g++
RM=rm -f
#CPPFLAGS=-g $(shell root-config --cflags)
#LDFLAGS=-g $(shell root-config --ldflags)
#LDLIBS=$(shell root-config --libs)

CPPFLAGS=-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -pedantic-errors -ggdb -O0 -std=c++23

# SRCS=array-of-pointers.cpp
#SRCS=01_address_of_variable.cpp
#SRCS=02_swap_values.cpp
#SRCS=03_array.cpp
#SRCS=04_void_pointer.cpp
#SRCS=05_what_is_null.cpp
#SRCS=06_pointer_to_pointer.cpp
#SRCS=07_pointer_to_array.cpp
#SRCS=08_array_of_pointers.cpp
SRCS=09_string.cc
OBJS=$(subst .cpp .cc,.o,$(SRCS))
#OBJS=$(subst .cpp,.o,$(SRCS))

all: cpp_executable 

cpp_executable: $(OBJS)
	$(CXX) $(CPPFLAGS) -o cpp_run $(OBJS)

#main.o: 


clean:
	$(RM) $(OBJS)

rebuild: clean all

distclean: clean
	$(RM) cpp_run
