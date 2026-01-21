<template>
	<view class="container">
		<view class="header">
			<input class="uni-input" placeholder="请输入" />
			<text>搜索</text>
		</view>
		<view class="content">
			<view class="left">
				<view class="itemStyle" v-for="item in categoryList" :key="item">
					<view>{{item.name}}</view>
				</view>
			</view>
			<view class="right"></view>
		</view>
	</view>
</template>

<script setup lang="ts">
	import { ref } from 'vue'

	const categoryList = ref([
		{ name: '时令推荐', value: 'seasonal' },
		{ name: '会员折扣', value: 'member_discount' },
		{ name: '鲜花绿植', value: 'flowers_plants' },
		{ name: '熟食面点', value: 'ready_meals' },
		{ name: '酒水饮料', value: 'beverages' },
		{ name: '休闲零食', value: 'snacks' },
		{name:'日用清洁',value:''},
		{name:'个护美妆',value:''},
		{name:'营养早餐',value:''},
		{ name: '年货集市', value: 'new_year_fair' }
	])
</script>

<style scoped lang="scss">
	.container {
		padding: 12rpx;
		background-color: #eafce6;
		.header {
			padding: 30rpx;
			border-radius: 20rpx;
			display: flex;
			justify-content: space-between;
			align-items: center;
			gap: 20rpx;

			.uni-input {
				background-color: #fff;
				width: 80%;
			}
		}
		.content{
			display: flex;
			padding:20rpx;
			background-color: #fff;
			border-radius: 20rpx;
			.left{
				width:200rpx;
				background-color: #f5f5f5;
				border-radius: 20rpx;
				.itemStyle{
					padding:30rpx;
					display: flex;
					justify-content: center;
					align-items: center;
				}
			}
			.right{
				flex:1;
			}
		}
	}
</style>