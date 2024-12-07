CC=gcc
CXX=g++
RM=rm -f
#CPPFLAGS=-g $(shell root-config --cflags)
#LDFLAGS=-g $(shell root-config --ldflags)
#LDLIBS=$(shell root-config --libs)

CPPFLAGS=-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 -std=c++23

SRCS=main.cc
OBJS=$(subst .cc,.o,$(SRCS))

all: cpp_executable test_shamima

cpp_executable: $(OBJS)
	$(CXX) $(CPPFLAGS) -o cpp_run $(OBJS)

main.o: main.cc

test_shamima:
	make -C testdir

clean:
	$(RM) $(OBJS)
	make clean -C testdir

rebuild: clean all

distclean: clean
	$(RM) cpp_run
