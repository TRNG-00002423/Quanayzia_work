import java.util.ArrayList;
import java.util.List;

public class VehicleDemo {

    public static void main(String[] args) {

        List<Vehicle> vehicles = new ArrayList<>();

        vehicles.add(
                new GasCar(
                        "Toyota",
                        2022,
                        7.5,
                        3.50));

        vehicles.add(
                new ElectricCar(
                        "Tesla",
                        2024,
                        18.0,
                        0.15));

        vehicles.add(
                new GasCar(
                        "Honda",
                        2021,
                        6.8,
                        3.50));

        for (Vehicle vehicle : vehicles) {

            System.out.printf(
                    "%s (%d) cost per 100km: $%.2f%n",
                    vehicle.getMake(),
                    vehicle.getModelYear(),
                    vehicle.fuelCostPer100Km());

            if (vehicle instanceof AutonomousCapable autonomous) {
                System.out.println(
                        "-Self-driving supported: "
                                + autonomous.supportsSelfDrive());
            }
        }

        // TODO: add GasCar, ElectricCar, optionally one that implements AutonomousCapable
        // TODO: polymorphic loop + instanceof demo
    }
}



