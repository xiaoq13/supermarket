<template>
	<view class="great_deal" :style="cardBackground">
		<view class="inner">
			<view class="header">
				<view class="hleft">
					{{title}}
				</view>
				<view class="hright">
					<text>更多</text>
					<uni-icons type="right"></uni-icons>
				</view>
			</view>
			<image :src="src" mode="heightFix" style="height: 240rpx;"></image>
			<view class="footer">{{productName}}</view>
		</view>
	</view>
</template>

<script setup>
	import {computed} from 'vue'
	const props = defineProps({
		title: {
			type: String,
			default: '默认标题'
		},
		src: {
			type: String,
			default: ''
		},
		productName: {
			type: String,
			default: ''
		},
		color: {
			type: String,
			default: ''
		}
	})
	
	const cardBackground = computed(()=>{
		return {background:`linear-gradient(to bottom,${props.color},#fff)`}
	})
	
</script>

<style scoped lang="scss">
	.great_deal {
		padding: 20rpx;
		height: 290rpx;
		border-radius: 20rpx;
		.inner{
			.header{
				font-size: 12px;
				display: flex;
				justify-content: space-between;
				.hleft{
					color:#f4074f;
					font-weight: 600;
				}
			}
			.footer{
				display: flex;
				justify-content: center;
				align-items: center;
				font-size: 12px;
			}
		}
	}
</style>