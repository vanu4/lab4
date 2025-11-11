package com.example.app;

import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test(groups = "math")
    public void testAdd() {
        Assert.assertEquals(calc.add(2, 3), 5);
    }

    @Test(groups = "math")
    public void testSubtract() {
        Assert.assertEquals(calc.subtract(5, 2), 3);
    }

    @Test(groups = "math")
    public void testMultiply() {
        Assert.assertEquals(calc.multiply(2, 4), 8);
    }

    @Test(groups = "math", expectedExceptions = IllegalArgumentException.class)
    public void testDivideByZero() {
        calc.divide(5, 0);
    }

    @Test(groups = "logic")
    public void testIsPositiveTrue() {
        Assert.assertTrue(calc.isPositive(10));
    }

    @Test(groups = "logic")
    public void testIsPositiveFalse() {
        Assert.assertFalse(calc.isPositive(-3));
    }

    @DataProvider(name = "dataForDivide")
    public Object[][] dataForDivide() {
        return new Object[][]{{6, 2, 3}, {10, 5, 2}};
    }

    @Test(dataProvider = "dataForDivide", groups = "math")
    public void testDivide(int a, int b, int result) {
        Assert.assertEquals(calc.divide(a, b), result);
    }
}
