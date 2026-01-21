<template>
	<view class="container">
		<view style="width: 100%; height: 420rpx; background-color: #f0f0f0;">
			<swiper :indicator-dots="true" :autoplay="true" :interval="3000" :duration="1000"
				style="width: 100%; height: 100%;">
				<swiper-item v-for="(item,index) in imgList" :key="index">
					<view class="swiper-item" style="width: 100%; height: 100%;">
						<image :src="item" mode="aspectFit" style="width: 100%; height: 100%;"></image>
					</view>
				</swiper-item>
			</swiper>
		</view>

		<view class="content">
			<view class="area" v-for="(item,index) in goodsType">
				<image class="pic" :src="item.src" mode="aspectFit" />
				<text class="" selectable>
					{{item.name}}
				</text>
			</view>
		</view>

		<view class="activity">
			<ActivityComp 
				title='天天特惠' 
				src="http://127.0.0.1:8000/uploads/6373ec81cdca4999986e723feb629cf7.jpeg"
				product-name="笔记本电脑"
				color="#fff5fd"
			/>
			
			<ActivityComp
				title='热卖榜单' 
				src="http://127.0.0.1:8000/uploads/cd58165da6244702a2deabba9cff1cc3.jpg"
				product-name="三只松鼠"
				color="#fffaf7"
			/>
		</view>
	</view>
</template>

<script setup lang='ts'>
	import {ref} from 'vue'
	import ActivityComp from '../../components/ActivityComp.vue'

	const imgList = ref([
		'http://127.0.0.1:8000/uploads/616b4c1fb3764a57965237637a09c5f3.jpg',
		'http://127.0.0.1:8000/uploads/a555b1b18eea49efa02de77732d52073.jpg',
		'http://127.0.0.1:8000/uploads/86d5bcc8f7a248669601d77dbfb15bfc.jpg'
	])

	const goodsType = ref([{
			name: '水果',
			src: '../../static/img/strawberry.png'
		},
		{
			name: '蔬菜',
			src: '../../static/img/shucai.png'
		},
		{
			name: '酒水',
			src: '../../static/img/jiushui.png'
		},
		{
			name: '护肤',
			src: '../../static/img/hufupin.png'
		},
		{
			name: '文具',
			src: '../../static/img/wenju.png'
		},
		{
			name: '零食',
			src: '../../static/img/lingshi.png'
		},
		{
			name: '面点',
			src: '../../static/img/miandian.png'
		},
		{
			name: '年货',
			src: '../../static/img/nianhuo.png'
		},
	])
</script>

<style scoped lang="scss">
	.container {
		display: flex;
		flex-direction: column;
		gap: 10rpx;
		.content {
			padding: 10rpx 20rpx;
			display: flex;
			gap: 30rpx;
			flex-wrap: wrap;
			justify-content: space-around;
			align-items: center;

			.area {
				width: 120rpx;
				height: 120rpx;
				border-radius: 30rpx;
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;

				.pic {
					background-color: #f8f8f8;
					box-sizing: border-box;
					padding: 10rpx;
					width: 100rpx;
					height: 100rpx;
					border-radius: 16rpx;
				}
			}
		}

		.activity {
			width: 100%;
			display: grid;
			grid-template-columns: 45% 45%;
			gap: 20rpx;
			padding: 20rpx;
		}
	}
</style>