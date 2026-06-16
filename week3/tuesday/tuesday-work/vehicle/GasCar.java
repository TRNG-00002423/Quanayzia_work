public class GasCar extends Vehicle {

    private double litersPer100Km;
    private double pricePerLiter;

    public GasCar(
            String make,
            int modelYear,
            double litersPer100Km,
            double pricePerLiter) {

        super(make, modelYear);

        this.litersPer100Km = litersPer100Km;
        this.pricePerLiter = pricePerLiter;
    }

    @Override
    public double fuelCostPer100Km() {
        return litersPer100Km * pricePerLiter;
    }
}