CC=gcc
CXX=g++
RM=rm -f
#CPPFLAGS=-g $(shell root-config --cflags)
#LDFLAGS=-g $(shell root-config --ldflags)
#LDLIBS=$(shell root-config --libs)

SRCS=hello_shoma.cc
OBJS=$(subst .cc,.o,$(SRCS))

#all: 

#cpp_executable: $(OBJS)
#	$(CXX) -o cpp_run $(OBJS)

hello_shoma.o: hello_shoma.cc

clean:
	$(RM) $(OBJS)

rebuild: clean all

distclean: clean
	$(RM) cpp_run
