cmake_minimum_required(VERSION 3.30)
set(CMAKE_C_COMPILER "C:\\MinGW\\bin\\gcc.exe")  
project(hello C)

add_subdirectory(lib)

add_executable(hello src/main.c)
target_link_libraries(video-app FFmpeg)