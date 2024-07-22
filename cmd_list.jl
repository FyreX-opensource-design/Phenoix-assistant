using JustSayIt
using JustSayIt.API
import cmd_functions

commands = Dict(
    "help"=> help_cmd(),
    "date"=> date(),
    "hey phoenix" => cmd_recgonize()
);

start(command=commands)