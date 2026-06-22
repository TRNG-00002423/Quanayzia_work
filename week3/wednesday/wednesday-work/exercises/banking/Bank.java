package banking;

import java.util.HashMap;

public class Bank {
    // TODO HashMap<String, Account>

    private HashMap<String,Account> hm;


    public void openAccount(String id, double initialDeposit) throws InvalidAccountException {

        if(id==null || id.isBlank()) throw new InvalidAccountException("Account ID cannot be blank");

        if(hm.containsKey(id)) throw new InvalidAccountException("Account already exists");

        hm.put(id,new Account(id,initialDeposit));

        //throw new UnsupportedOperationException("TODO");
    }

    public Account getAccount(String id) throws InvalidAccountException {

        Account account = hm.get(id);

        if (account == null) {
            throw new InvalidAccountException("Account not found");
        }

        return account;

        //throw new UnsupportedOperationException("TODO");
    }

    public void transfer(String fromId, String toId, double amount)
            throws InvalidAccountException, InsufficientFundsException {


        Account from=getAccount(fromId);
        Account to=getAccount(toId);

        from.withdraw(amount);
        to.deposit(amount);

        //throw new UnsupportedOperationException("TODO");
    }
}