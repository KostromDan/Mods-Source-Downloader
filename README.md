# Mods-Source-Downloader

Downloads sources of all mods from manifest file of your modpack.
If mod is on github, source will be dowloaded from github.
If it's impossible to find source, mod will be decompiled from jar.

## ⚠️ WARNING ⚠️: You CANNOT publish any code generated by this tool.
## ⚠️ WARNING ⚠️: Check license of all mods form manifest file or usage of this tool can be eligible and cause license infringement

## Intructions:

### 1
install requirements:
```pip install -r requirements.txt```

rename ```tokens.example.py``` to ```tokens.py``` and paste your actual github token.
### 2
run ```1_get_repo_links.py```

select manifest file in file dialog

run ```2_get_branches.py```
### 3
Go ```3_choose_correct_branch.py```

If you run different from 1.19.2 version, clear ```accepted_options```

Run ```3_choose_correct_branch.py```

Until you getting such msg:

```
Can't select branch from:
['1.14',
 '1.15',
 '1.16',
 '1.16.2',
 '1.17',
 '1.18',
 '1.18.2',
 '1.19',
 '1.19.3',
 '1.19.4',
 '1.20']
Add one of these to accepted_options
```
Keep adding to ```accepted_options``` one of branch variants and rerun script.

### 4

Run ```4_clone_all_found.py```

Run ```5_copy_non_open_source_mods.py```

Select mods folder of your modpack in dir dialog.

Run ```6_decompile_non_open_source_mods.py```

### Done!

Open as project ```result``` dir.




