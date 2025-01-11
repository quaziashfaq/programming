CC=gcc
CXX=g++
RM=rm -f
#CPPFLAGS=-g $(shell root-config --cflags)
#LDFLAGS=-g $(shell root-config --ldflags)
#LDLIBS=$(shell root-config --libs)

CPPFLAGS=-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -pedantic-errors -ggdb -O0 -std=c++23

SRCS=array-of-pointers.cpp
OBJS=$(subst .cpp .cc,.o,$(SRCS))

all: cpp_executable 

cpp_executable: $(OBJS)
	$(CXX) $(CPPFLAGS) -o cpp_run $(OBJS)

main.o: array-of-pointers.cpp


clean:
	$(RM) $(OBJS)

rebuild: clean all

distclean: clean
	$(RM) cpp_run
