import dateBuilder from "../utils/dateBuilder";
import { HealthResponse, ServiceHealth } from "./health.model";

export default class HealthService {
  getOverallHealth() {
    const overallHealth: HealthResponse = {
      name: "smarter-bullets",
      status: true,
      timeStamp: Date.now().toString(),
      serviceStatuses: this.getAllServicesHealth(),
    };
    return overallHealth;
  }

  private getAllServicesHealth(): Array<ServiceHealth> {
    return [{ name: "thisIsAnExample", status: true, timeStamp: dateBuilder() }];
  }
}
