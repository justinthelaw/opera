import { TIMEZONE } from "../constants/server.constants";

export default function dateBuilder(): string {
  const time = new Date().toISOString();

  const timeString = new Date(time).toLocaleString("en-US", {
    timeZone: TIMEZONE,
    hour12: false,
  });

  return `${timeString} (${TIMEZONE})`
}
