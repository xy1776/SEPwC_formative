suppressPackageStartupMessages({
library(testthat)
})

# Run like:
#jh1889@mirovia:~/work/teaching/SEPwC_assessments/sediment_assessment/test$ Rscript test_script.R 
# Test passed 🥇
# Test passed 🌈
# Test passed 🎊
# Test passed 🥳
# ── Warning: check main# 
# ...
#

# load in the script you want to test
source("../todo.R")
test_data <- "test_list.txt"


# tests --------------------
# check the get_plot_limit function
  test_that("list_tasks", {
    TASK_FILE <- ""
  })

  test_that("remove_task", {
    
    
  })

  test_that("add_task", {

    
  })

  test_that("check main", {
      args <- c("list"=TRUE)
      args <- data.frame(t(args))
      main(args)
  })


  if (requireNamespace("lintr")) {
    library(lintr)
  
    context("linting script")
    test_that("Coding style", {
      output<-lintr::lint("../todo.R")
      expect_lt(length(output),500)
      expect_lt(length(output),400)
      expect_lt(length(output),250)
      expect_lt(length(output),100)
      expect_lt(length(output),50)
      expect_lt(length(output),10)
      expect_equal(length(output),0)
    })
  }


