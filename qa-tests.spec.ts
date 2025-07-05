import { test, expect } from '@playwright/test';

test.describe('QA Agent Auto Tests', () => {
  test('Sign up with valid email and password', async ({ page }) => {
    await page.goto('https://recruter.ai/signup');
    await page.fill('#email', 'test@example.com');
    await page.fill('#password', 'StrongP@ss1');
    await page.click('#signup');
    await expect(page).toHaveURL(/dashboard/);
  });
});
