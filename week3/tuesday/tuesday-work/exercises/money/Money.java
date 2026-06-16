package money;

import java.util.Objects;

/**
 * TODO: immutable currency + amountMinor; equals/hashCode contract.
 */
public final class Money {
    // TODO fields, constructor validates currency non-null

    private final String currency;
    private final long amountMinor;

    public Money(String currency, long amountMinor) {
        if (currency == null) {
            throw new IllegalArgumentException("currency cannot be null");
        }

        this.currency = currency;
        this.amountMinor = amountMinor;
    }


    // TODO getters


    public String getCurrency() {
        return currency;
    }

    public long getAmountMinor() {
        return amountMinor;
    }

    @Override
    public boolean equals(Object o) {

        if (this == o) return true;
        if (!(o instanceof Money)) return false;

        Money money = (Money) o;

        return amountMinor == money.amountMinor
                && currency.equals(money.currency);

        //throw new UnsupportedOperationException("TODO");
    }

    @Override
    public int hashCode() {
        return Objects.hash(currency, amountMinor);
        //throw new UnsupportedOperationException("TODO");
    }

    @Override
    public String toString() {

        return "Money{" +
                "currency='" + currency + '\'' +
                ", amountMinor=" + amountMinor +
                '}';
        //throw new UnsupportedOperationException("TODO");
    }
}