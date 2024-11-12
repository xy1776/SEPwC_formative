#!/usr/bin/env Rscript
suppressPackageStartupMessages({
library(argparse)
})

TASK_FILE <- ".tasks.txt"

add_task <- function(task) {


}

list_tasks <- function(task) {


}

remove_task <- function(index) {


}

main <- function(args) {

    print(args)
        
    if (args$add) {
        add_task(args$add)
    } else if (args$list) {
        tasks <- list_tasks()
        print(tasks)
    } else if (args$remove) {
        remove_task(args$remove)
    } else {
        print("Use --help to get help on using this program")
    }
    
}


if(sys.nframe() == 0) {

  # main program, called via Rscript
  parser = ArgumentParser(
                    description="Command-line Todo List"
                    )
  parser$add_argument('-a', '--add',
                    help="Add a new task")
  parser$add_argument('-l', '--list',
                    action='store_true',
                    help="List all tasks")
  parser$add_argument('-r', '--remove',
                    help="Remove a task by index")

  args = parser$parse_args()  
  main(args)
}
