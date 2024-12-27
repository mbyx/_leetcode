#include <stdio.h>
#include <stdbool.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, x, y;
        scanf("%d %d %d", &n, &x, &y);
        int a[n];

        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        int price_without_discount = 0;
        for (int i = 0; i < n; i++) {
            price_without_discount += a[i];
        }

        int price_with_discount = x;
        for (int i = 0; i < n; i++) {
            int discounted_price = a[i] - y;
            price_with_discount += discounted_price <= 0? 0: discounted_price;
        }

        bool should_buy_coupon = price_with_discount < price_without_discount;
        printf(should_buy_coupon? "COUPON\n": "NO COUPON\n");
    }

    return 0;
}
