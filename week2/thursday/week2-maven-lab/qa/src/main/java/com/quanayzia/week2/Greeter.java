package com.quanayzia.week2;


//method String hello(String name) returns "Hello, " + name (non-blank names only;
// throw IllegalArgumentException if blank).

public class Greeter {

    public String hello(String name){



        if(name.isBlank()){

            throw new IllegalArgumentException();
        }

        return "Hello "+ name;
    }
}
