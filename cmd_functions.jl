using JustSayIt
using JustSayIt.API
using variables

python = "phoenix/bin/python"
voice_out = python * " import base_cmds.py && "
variables.variables()

function date()
    if global help && listen == true
        `$voice_out base_cmds.say_help("time")`
        global help = false 
    elseif help == false && listen == true
    `$voice_out base_cmds.say_date()`
    global listen = false
    end 
end

# essential cmds here

function cmd_help()
    global help = true
    `$voice_out base_cmds.say_help_enabled()`
end

function cmd_recgonize()
    global listen = true
    `$voice_out base_cmds.listen()`
end