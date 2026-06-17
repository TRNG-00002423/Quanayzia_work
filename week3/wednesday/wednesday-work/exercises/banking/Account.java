package banking;

public class Account {
    // TODO fields: id, balance

    private final String id;

    private double balance;


    public Account(String id, double balance) {
        this.id = id;
        this.balance=balance;
    }


    public void deposit(double amount) {

        if(amount <=0){
            throw new IllegalArgumentException("Value must be greater then 0");
        }
        balance+=amount;
    }

    public void withdraw(double amount) throws InsufficientFundsException {

        if(amount >balance){
            throw new InsufficientFundsException("You are broke!!!!");
        }

        balance-=amount;

        //throw new UnsupportedOperationException("TODO");
    }
}