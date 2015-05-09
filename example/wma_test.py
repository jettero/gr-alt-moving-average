#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: wma-test
# Author: Paul Miller
# Description: test wma
# Generated: Sat May  9 08:27:07 2015
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import gr_alt_moving_average
import sip
import sys

class wma_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "wma-test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("wma-test")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wma_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000
        self.noise_amp = noise_amp = 0
        self.alpha = alpha = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._noise_amp_layout = Qt.QVBoxLayout()
        self._noise_amp_tool_bar = Qt.QToolBar(self)
        self._noise_amp_layout.addWidget(self._noise_amp_tool_bar)
        self._noise_amp_tool_bar.addWidget(Qt.QLabel("noise_amp"+": "))
        self._noise_amp_counter = Qwt.QwtCounter()
        self._noise_amp_counter.setRange(0, 1, 0.1)
        self._noise_amp_counter.setNumButtons(2)
        self._noise_amp_counter.setValue(self.noise_amp)
        self._noise_amp_tool_bar.addWidget(self._noise_amp_counter)
        self._noise_amp_counter.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_amp_slider.setRange(0, 1, 0.1)
        self._noise_amp_slider.setValue(self.noise_amp)
        self._noise_amp_slider.setMinimumWidth(200)
        self._noise_amp_slider.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_layout.addWidget(self._noise_amp_slider)
        self.top_layout.addLayout(self._noise_amp_layout)
        self._alpha_layout = Qt.QVBoxLayout()
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_layout.addWidget(self._alpha_tool_bar)
        self._alpha_tool_bar.addWidget(Qt.QLabel("alpha"+": "))
        self._alpha_counter = Qwt.QwtCounter()
        self._alpha_counter.setRange(0, 1, 0.1)
        self._alpha_counter.setNumButtons(2)
        self._alpha_counter.setValue(self.alpha)
        self._alpha_tool_bar.addWidget(self._alpha_counter)
        self._alpha_counter.valueChanged.connect(self.set_alpha)
        self._alpha_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._alpha_slider.setRange(0, 1, 0.1)
        self._alpha_slider.setValue(self.alpha)
        self._alpha_slider.setMinimumWidth(200)
        self._alpha_slider.valueChanged.connect(self.set_alpha)
        self._alpha_layout.addWidget(self._alpha_slider)
        self.top_layout.addLayout(self._alpha_layout)
        self.wmoving_0 = gr_alt_moving_average.wmoving(alpha=alpha)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	samp_rate, #size
        	samp_rate, #samp_rate
        	"QT GUI Plot", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-(3+noise_amp), 3+noise_amp)
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	samp_rate, #size
        	samp_rate, #samp_rate
        	"QT GUI Plot", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate * samp_rate)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 13, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_IMPULSE, noise_amp, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wmoving_0, 0))
        self.connect((self.wmoving_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_time_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wma_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate * self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self._noise_amp_counter.setValue(self.noise_amp)
        self._noise_amp_slider.setValue(self.noise_amp)
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)
        self.qtgui_time_sink_x_0_0.set_y_axis(-(3+self.noise_amp), 3+self.noise_amp)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self._alpha_counter.setValue(self.alpha)
        self._alpha_slider.setValue(self.alpha)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = wma_test()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

