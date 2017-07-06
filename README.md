## Install

There are two ways to get the VM:

1. Build VM manually; it takes ~20 minutes with moderate networking condition. (Dependencies: [vagrant](https://www.vagrantup.com/),
   [virtualbox](https://www.virtualbox.org/))

```
$ ls
benchmarks  oopsla_data  otp-default  otp-msg  otp-systemtap  README.md  run  Vagrantfile
$ vagrant destroy -f; vagrant up
```

2. Download the pre-built [VM image](https://drive.google.com/file/d/0BwHr-qTTh38ZZTRsOF92cmFZMk0/view). Then, unzip it and you can run the VM using
   Virtual Box. (Dependency: [virtualbox](https://www.virtualbox.org/))

## Orca related files

Inside `ponyc` folder:

- `try_gc` in `src/libponyrt/actor/actor.c` is the entry point for starting a GC cycle.
- `handle_message` in `src/libponyrt/actor/actor.c` shows how Orca related messages are processed.
- `ponyint_gc_sendobject` in `~/github/ponyc/src/libponyrt/gc/gc.c` is for tracing on sending objects across actors; similar tracing code for
  receiving objects, sending & receiving actors, etc. can be found in the same file as well.
- `src/libponyrt/mem/heap.[h|c]` contain actor-local heap.
