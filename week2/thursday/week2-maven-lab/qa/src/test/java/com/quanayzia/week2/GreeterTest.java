package com.quanayzia.week2;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class GreeterTest {


    @Test
    public void happyPath(){

        Greeter greet=new Greeter();

        String name= "Nay";
        String greeting=greet.hello(name);

        assertEquals("Hello Nay",greeting);
        assertThrows(IllegalArgumentException.class, () -> greet.hello(""));
    }

@Test
    public void testException(){

        Greeter greet=new Greeter();

        assertThrows(IllegalArgumentException.class, () -> greet.hello(""));
    }
}
