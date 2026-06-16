public class ElectricCar extends Vehicle
        implements AutonomousCapable {

    private double kWhPer100Km;
    private double pricePerKWh;

    public ElectricCar(
            String make,
            int modelYear,
            double kWhPer100Km,
            double pricePerKWh) {

        super(make, modelYear);

        this.kWhPer100Km = kWhPer100Km;
        this.pricePerKWh = pricePerKWh;
    }

    @Override
    public double fuelCostPer100Km() {
        return kWhPer100Km * pricePerKWh;
    }

    @Override
    public boolean supportsSelfDrive() {
        return true;
    }
}