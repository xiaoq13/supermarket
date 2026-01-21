"use strict";
const common_vendor = require("../common/vendor.js");
if (!Array) {
  const _easycom_uni_icons2 = common_vendor.resolveComponent("uni-icons");
  _easycom_uni_icons2();
}
const _easycom_uni_icons = () => "../uni_modules/uni-icons/components/uni-icons/uni-icons.js";
if (!Math) {
  _easycom_uni_icons();
}
const _sfc_main = {
  __name: "CardComp",
  props: {
    title: {
      type: String,
      default: "默认标题"
    },
    src: {
      type: String,
      default: ""
    },
    productName: {
      type: String,
      default: ""
    },
    color: {
      type: String,
      default: ""
    }
  },
  setup(__props) {
    const props = __props;
    const cardBackground = common_vendor.computed(() => {
      return { background: `linear-gradient(to bottom,${props.color},#fff)` };
    });
    return (_ctx, _cache) => {
      return {
        a: common_vendor.t(__props.title),
        b: common_vendor.p({
          type: "right"
        }),
        c: __props.src,
        d: common_vendor.t(__props.productName),
        e: common_vendor.s(cardBackground.value)
      };
    };
  }
};
const Component = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["__scopeId", "data-v-587c6646"]]);
wx.createComponent(Component);
//# sourceMappingURL=../../.sourcemap/mp-weixin/components/CardComp.js.map
