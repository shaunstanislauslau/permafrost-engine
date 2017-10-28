CC		= gcc
AR		= ar
BIN		= ./bin/pf

PF_DIRS = ./src ./src/render ./src/anim
PF_SRCS = $(foreach dir,$(PF_DIRS),$(wildcard $(dir)/*.c)) 
PF_OBJS = $(PF_SRCS:./src/%.c=./obj/%.o)
PF_DEPS = $(PF_OBJS:%.o=%.d)

CFLAGS  = -std=c99 -I./include -g
DEFS  	=
LDFLAGS = -lGL -lGLEW -lSDL2 -lm

./obj/%.o: ./src/%.c
	@mkdir -p ./obj
	$(CC) -MT $@ -MMD -MP -MF ./obj/$*.d $(CFLAGS) $(DEFS) -c $< -o $@

pf: $(PF_OBJS)
	@mkdir -p ./bin
	$(CC) $? -o $(BIN) $(LDFLAGS)

-include $(PF_DEPS)

.PHONY: clean

clean:
	@rm -rf $(PF_OBJS) $(PF_DEPS) $(BIN)

