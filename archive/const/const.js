// optimization status codes
// status codes for optimization direction
export const enum STATUS {
  OPTIMIZED = 0,
  FAILED_OPT = 1,
  NOT_OPT = -1,
  MAX_UNDERFLOW = -4,
}
interface Form {
  fields: string[];
  likelyWidth: string;
}
// could not do a static class property because of MS edge
interface Forms {
  all: {
    [key: string]: Form;
  };
}
const Forms: Forms = {
  all: {
    AF707: {
      fields: [
        "S2DutyTitleDesc",
        "S4Assessment",
        "S5Assessment",
        "S6Assessment",
      ],
      likelyWidth: "201.041mm",
    },
    AF1206: {
      fields: ["specificAccomplishments", "p2SpecificAccomplishments"],
      likelyWidth: "202.321mm",
    },
    AF910: {
      fields: [
        "KeyDuties",
        "IIIComments",
        "IVComments",
        "VComments",
        "VIIIComments",
        "IXComments",
      ],
      likelyWidth: "202.321mm",
    },
    AF911: {
      fields: [
        "KeyDuties",
        "IIIComments",
        "IVComments",
        "VIIComments",
        "VIIIComments",
        "IXComments",
      ],
      likelyWidth: "202.321mm",
    },
    DAF707: {
      fields: [
        "S2DutyTitleDesc",
        "S4Assessment",
        "S5Assessment",
        "S6Assessment",
      ],
      likelyWidth: "201.041mm",
    },
    DAF1206: {
      fields: ["specificAccomplishments", "p2SpecificAccomplishments"],
      likelyWidth: "202.321mm",
    },
    DAF910: {
      fields: [
        "KeyDuties",
        "IIIComments",
        "IVComments",
        "VComments",
        "VIIIComments",
        "IXComments",
      ],
      likelyWidth: "202.321mm",
    },
    DAF911: {
      fields: [
        "KeyDuties",
        "IIIComments",
        "IVComments",
        "VIIComments",
        "VIIIComments",
        "IXComments",
      ],
      likelyWidth: "202.321mm",
    },
  },
};
export {Forms};
