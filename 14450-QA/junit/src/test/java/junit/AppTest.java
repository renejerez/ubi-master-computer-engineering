package junit;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;

/**
 * Unit test for simple App.
 */
public class AppTest {
    /**
     * Rigorous Test.
     */
    private Calculator calculator;

   @BeforeEach

      void setUp() {

      calculator = new Calculator();
      }

@Test
   void testAdd() {

      int result = calculator.add(5, 3);
      Assertions.assertEquals(8, result);
   }

   
@Test
   void testSubtract() {   
      int result = calculator.subtract(10, 4);
      Assertions.assertEquals(6, result);
   }

@Test
void testMultiply() {
   int result = calculator.multiply(2, 5);
   Assertions.assertEquals(10, result);
   }

@Test
void testDivide() {
   double result = calculator.divide(10, 2);
   Assertions.assertEquals(11, result);
   } 
   
}
