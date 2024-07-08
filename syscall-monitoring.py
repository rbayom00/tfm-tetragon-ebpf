#!/usr/bin/python3
from bcc import BPF

program = """
TRACEPOINT_PROBE(raw_syscalls,sys_enter) {
    if (args->id==59){
        bpf_trace_printk("Ejecutada la syscall execve con id: %d\\n Desde: %s\\n",args->id,args->args[0]);
    }
    return 0;
}
"""

b = BPF(text=program)
b.trace_print()