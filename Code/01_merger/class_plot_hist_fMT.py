#!/usr/bin/env python
# coding: utf-8

# # FIRST ASSIGNMENT
#
# **GROUP: EARTHQUAKES**
#
# Guadagnini Michele - 1230663
#
# Lambertini Alessandro - 1242885
#
# Pagano Alice - 1236916
#
# Puppin Michele - 1227474


# Import main packages
import os
import pandas as pd
import numpy as np
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
import bokeh.palettes as palette # For palette of colors

class plot_hist_fMT:



    def mass_1(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index
        fig.suptitle('Plots of distribution of mass m1',fontsize=30)        
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):               
                edge = np.logspace(np.log10(df[i][j]['m1form[8]'].min()), np.log10(df[i][j]['m1form[8]'].max()), 30)
                sns.distplot(df[i][j]['m1form[8]'],bins=edge,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of mass m1 for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('m1 $[M_\odot]$',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16)
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)
            ax[i].set_xscale('log')
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)

        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_mass_1.pdf', format='pdf')
        plt.close()



    def mass_2(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index
        fig.suptitle('Plots of distribution of mass m2',fontsize=30)
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):
                edge = np.logspace(np.log10(df[i][j]['m2form[10]'].min()), np.log10(df[i][j]['m2form[10]'].max()), 30)
                sns.distplot(df[i][j]['m2form[10]'],bins=edge,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of mass m2 for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('m2 $[M_\odot]$',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16)
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)            
            ax[i].set_xscale('log')
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)

        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_mass_2.pdf', format='pdf')
        plt.close()



    def mass_chirp(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index
        fig.suptitle('Plots of distribution of mass mchirp',fontsize=30)
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):
                # Compute m_chirp
                mchirp = np.power( df[i][j]['m1form[8]']*df[i][j]['m2form[10]'], 3/5)/np.power( df[i][j]['m1form[8]']*df[i][j]['m2form[10]'], 1/5)
                edge = np.logspace(np.log10(mchirp.min()), np.log10(mchirp.max()), 30)
                sns.distplot(mchirp,bins=edge,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of mass mchirp for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('mchirp $[M_\odot]$',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16)
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)
            ax[i].set_xscale('log')
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)

        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_mass_chirp.pdf', format='pdf')
        plt.close()



    def mass_tot(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index
        fig.suptitle('Plots of distribution of mass mtot',fontsize=30)
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):
                # Compute m_tot
                mtot = df[i][j]['m1form[8]'] + df[i][j]['m2form[10]']
                edge = np.logspace(np.log10(mtot.min()), np.log10(mtot.max()), 30)
                sns.distplot(mtot,bins=edge,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of mass mtot for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('mtot $[M_\odot]$',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16)
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)
            ax[i].set_xscale('log')
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)

        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_mass_tot.pdf', format='pdf')
        plt.close()



    def q(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index
        fig.suptitle('Plots of distribution of q',fontsize=30)
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):
                # Compute q
                q = df[i][j]['m2form[10]']/df[i][j]['m1form[8]']
                sns.distplot(q,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of q for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('q',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16,loc='upper left')
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)

        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_q.pdf', format='pdf')
        plt.close()



    def t_merg(self,df,fMT,metal): #(dataframe,fMT,metal)

        fig = plt.figure(figsize=(30,30))
        ax = [fig.add_subplot(3,3,s) for s in range(1,len(fMT)+1)] #nrows,ncols,index        
        fig.suptitle('Plots of distribution of time tmerg',fontsize=30)
        col = sns.color_palette(palette.viridis(len(metal)))

        for i in range(0,len(fMT)):
            for j in range(0,len(metal)):

                edge = 50*np.logspace(np.log10(df[i][j]['tmerg[11]'].min()), np.log10(df[i][j]['tmerg[11]'].max()), 30) 

                sns.distplot(df[i][j]['tmerg[11]'],bins=edge,kde=False,norm_hist=True,label=metal[j], 
                                hist_kws={"histtype": "step","lw": 2},ax=ax[i],color=col[j])

            ax[i].set_title('Distribution of time tmerg for fMT={}'.format(fMT[i]),fontsize=18)
            ax[i].set_xlabel('tmerg [Myr]',fontsize=18)
            ax[i].set_ylabel('Density',fontsize=18)
            ax[i].legend(title='Metallicity',fontsize=14,title_fontsize=16)
            ax[i].tick_params(axis="x", labelsize=16)
            ax[i].tick_params(axis="y", labelsize=16)
            ax[i].set_xscale('log')
            ax[i].set_yscale('log')
            ax[i].grid(True, which="both", ls="-",color='0.93')
            ax[i].set_axisbelow(True)           
            
        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/hist_time_tmerg.pdf', format='pdf')
        plt.close()



    def flip_fraction(self,df,fMT,metal):
        # Plot fraction of flipped mass as function of fMT

        num = []
        den = []

        for i in range(0,len(fMT)):
            a = 0
            b = 0
            for j in range(0,len(metal)):
                    a += sum(df[i][j]['flip_mask'])
                    b += df[i][j]['flip_mask'].shape[0]
            num.append(a)
            den.append(b)
                
        x_fMT = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7,1.0]
        frac = np.array(num)/np.array(den)

        fig, ax = plt.subplots(figsize=(10,10))
        plt.plot(x_fMT,frac,'o',color='#440154')
        ax.set_title('Fraction of flipped masses',fontsize=18)
        ax.set_xlabel('fMT',fontsize=18)
        ax.set_ylabel('Fraction',fontsize=18)
        ax.tick_params(axis="x", labelsize=16)
        ax.tick_params(axis="y", labelsize=16)
        ax.grid(True, which="both", ls="-",color='0.93')
        ax.set_axisbelow(True)           
                    
        if not os.path.isdir('./hist_fMT'):
            os.mkdir('./hist_fMT')

        plt.savefig('hist_fMT/fraction_fMT.pdf', format='pdf')
        plt.close()




















