"use strict";
const common_vendor = require("../../common/vendor.js");
if (!Math) {
  CardComp();
}
const CardComp = () => "../../components/CardComp.js";
const _sfc_main = /* @__PURE__ */ common_vendor.defineComponent({
  __name: "home",
  setup(__props) {
    const imgList = common_vendor.ref([
      "http://127.0.0.1:8000/uploads/616b4c1fb3764a57965237637a09c5f3.jpg",
      "http://127.0.0.1:8000/uploads/a555b1b18eea49efa02de77732d52073.jpg",
      "http://127.0.0.1:8000/uploads/86d5bcc8f7a248669601d77dbfb15bfc.jpg"
    ]);
    const goodsType = common_vendor.ref([
      {
        name: "水果",
        src: "../../static/img/strawberry.png"
      },
      {
        name: "蔬菜",
        src: "../../static/img/shucai.png"
      },
      {
        name: "酒水",
        src: "../../static/img/jiushui.png"
      },
      {
        name: "护肤",
        src: "../../static/img/hufupin.png"
      },
      {
        name: "文具",
        src: "../../static/img/wenju.png"
      },
      {
        name: "零食",
        src: "../../static/img/lingshi.png"
      },
      {
        name: "面点",
        src: "../../static/img/miandian.png"
      },
      {
        name: "年货",
        src: "../../static/img/nianhuo.png"
      }
    ]);
    return (_ctx, _cache) => {
      return {
        a: common_vendor.f(imgList.value, (item, index, i0) => {
          return {
            a: item,
            b: index
          };
        }),
        b: common_vendor.f(goodsType.value, (item, index, i0) => {
          return {
            a: item.src,
            b: common_vendor.t(item.name)
          };
        }),
        c: common_vendor.p({
          title: "天天特惠",
          src: "http://127.0.0.1:8000/uploads/6373ec81cdca4999986e723feb629cf7.jpeg",
          ["product-name"]: "笔记本电脑",
          color: "#fff5fd"
        }),
        d: common_vendor.p({
          title: "热卖榜单",
          src: "http://127.0.0.1:8000/uploads/cd58165da6244702a2deabba9cff1cc3.jpg",
          ["product-name"]: "三只松鼠",
          color: "#fffaf7"
        })
      };
    };
  }
});
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["__scopeId", "data-v-07e72d3c"]]);
wx.createPage(MiniProgramPage);
//# sourceMappingURL=../../../.sourcemap/mp-weixin/pages/home/home.js.map
