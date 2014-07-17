#!/bin/sh

bash -i -c "sudo noip2 &"
bash -i -c "cd ~/data/gitno/github/boykov.github.io/ && jekyll -w serve &"
bash -i -c "~/bin/cloud &"
