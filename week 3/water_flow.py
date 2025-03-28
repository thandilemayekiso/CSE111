# Import necessary modules
import math

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal seconds

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters / second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters / second


# Functions
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate pressure loss due to pipe fittings."""
    return -0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate Reynolds number for given pipe conditions."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate pressure loss due to a reduction in pipe diameter."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * (fluid_velocity ** 2) / 2000


def kpa_to_psi(kpa):
    """Convert kilopascals to psi."""
    return kpa * 0.145038


def main():
    """Main function to run the water pressure calculations."""
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    # Initial pressure calculations
    diameter = PVC_SCHED80_INNER_DIAMETER
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    pressure = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)

    # Final pressure calculation at house
    diameter = HDPE_SDR11_INNER_DIAMETER
    velocity = HOUSEHOLD_VELOCITY
    print(f"Pressure at house: {pressure:.1f} kilopascals ({kpa_to_psi(pressure):.1f} psi)")


if __name__ == "__main__":
    main()

